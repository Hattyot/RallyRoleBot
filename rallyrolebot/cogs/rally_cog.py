import json
import sys
import traceback
from typing import Union

import discord
from discord.ext import commands, tasks
from discord.utils import get

import data
import rally_api
import coingecko_api
import validation
import errors

from utils import pretty_print, send_to_dm, get_gradient_by_percentage
from utils.converters import CreatorCoin, CommonCoin
from constants import *


class RallyCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def cog_after_invoke(self, ctx):
        await pretty_print(
            ctx, "Command completed successfully!", title="Success", color=SUCCESS_COLOR
        )

    @errors.standard_error_handler
    async def cog_command_error(self, ctx, error):

        # All other Errors not returned come here. And we can just print the default TraceBack.
        print("Ignoring exception in command {}:".format(ctx.command), file=sys.stderr)
        traceback.print_exception(
            type(error), error, error.__traceback__, file=sys.stderr
        )

    @commands.command(name="set_rally_id", help="Set your rally id")
    @commands.dm_only()
    async def set_rally_id(self, ctx, rally_id):
        data.add_discord_rally_mapping(ctx.author.id, rally_id)

    @commands.command(name="price", help="Get the price data of a coin")
    async def price(self, ctx, coin_symbol : Union[CreatorCoin, CommonCoin]):
        def get_gradient_color(percentage):
            if percentage < 0:
                return get_gradient_by_percentage(str(WHITE_COLOR), str(DARK_RED_COLOR), PRICE_GRADIENT_DEPTH, abs(percentage))
            else:
                return get_gradient_by_percentage(str(WHITE_COLOR), str(DARK_GREEN_COLOR), PRICE_GRADIENT_DEPTH, percentage)

        price = coingecko_api.get_price_data(coin_symbol) or rally_api.get_price_data(coin_symbol)

        percentage_24h = price["price_change_percentage_24h"]
        percentage_30d = price["price_change_percentage_30d"]

        if price is False:
            raise errors.RequestError("There was an error while fetching the coin data")
        else:
            await pretty_print(ctx, 
                f"Current Price: {price['current_price']}", 
                title="Current Price", 
                color=WHITE_COLOR)
            await pretty_print(ctx, 
                f"{percentage_24h}%", 
                title="24H Price Change", 
                color=get_gradient_color(percentage_24h))
            await pretty_print(ctx, 
                f"{percentage_30d}%", 
                title="30D Price Change", 
                color=get_gradient_color(percentage_30d))

    @commands.command(name="unset_rally_id", help="Unset your rally id")
    @commands.dm_only()
    async def unset_rally_id(self, ctx, rally_id):
        data.remove_discord_rally_mapping(ctx.author.id, rally_id)

    @commands.command(
        name="admin_unset_rally_id",
        help=" <discord ID> <rally ID> Unset rally ID to discord ID mapping",
    )
    @validation.owner_or_permissions(administrator=True)
    async def admin_unset_rally_id(self, ctx, discord_id: discord.User, rally_id):
        data.remove_discord_rally_mapping(discord_id, rally_id)

  
