from ...utils import text_response, User, server_id_2_server_name, server_name_2_server_id, server_exists, config
import tsugu_api_async
from arclet.alconna import Alconna, Option, Subcommand, Args, CommandMeta, Empty, Namespace, namespace, MultiVar


async def handler(message: str, user: User, platform: str, channel_id: str):
    res = Alconna(
        ["查曲"],
        Args["word#歌曲信息，名称，乐队，难度等。", MultiVar(str)],
        meta=CommandMeta(
            compact=config.compact, description="查曲",
            usage='根据关键词或曲目ID查询曲目信息。',
            example='''查曲 1 :返回1号曲的信息
查曲 ag lv27 :返回所有难度为27的ag曲列表
查曲 >27 :查询大于27的曲目
查曲 滑滑蛋 :匹配歌曲 fuwa fuwa time'''
        )
    ).parse(message)

    if res.matched:
        return await tsugu_api_async.search_song(user.default_server, " ".join(res.word))

    return res

