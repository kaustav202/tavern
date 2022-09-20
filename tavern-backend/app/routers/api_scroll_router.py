from typing import List
from fastapi import APIRouter, HTTPException, status

from config import SETTINGS
from models.scroll_model import Scroll
from services.core_service import CoreService


api_scroll = APIRouter()
core_service = CoreService()


@api_scroll.get('/', status_code=status.HTTP_200_OK)
async def get_scrolls() -> List[Scroll]:
    """Get a list of all scrolls.
    Args:
        None
    Returns:
        List[Scroll]: A list of scrolls.
    Raises:
        HTTPException: If an error occurs
    """
    scroll_list = []
    try:
        if not SETTINGS.APP_DEBUG:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN, detail='Forbidden')

        # TODO: add service
        scroll_list = core_service.get_scrolls()

    except HTTPException as e:
        raise e

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    return scroll_list
