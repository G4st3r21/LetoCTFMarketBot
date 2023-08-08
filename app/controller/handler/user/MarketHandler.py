from operator import attrgetter
from typing import List, Dict

from aiogram.types import Chat

from app.api.dto.score import UserScoreResponse, TeamScoreResponse
from app.api.service import ScoreService, UserService
from app.database import User


class MarketHandler:
    @staticmethod
    async def profile_score(event_chat: Chat, **kwargs) -> Dict:
        user: User = User.get_or_none(User.chat_id == event_chat.id)
        profile = await ScoreService.profile_score(user.id)
        return profile.data.as_json()

    @staticmethod
    async def category_menu(event_chat: Chat, **kwargs) -> Dict:
        user: User = User.get_or_none(User.chat_id == event_chat.id)
        profile = await ScoreService.profile_score(user.id)
        pass


