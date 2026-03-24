import httpx
from fastapi import HTTPException

from app.core.config import settings
from app.utils import custom_response

class UserServiceIntegration:
    """Handles communication with the User Service."""

    @staticmethod
    async def get_user_info(user_id: int, token: str) -> dict:
        """
        Fetches user info from the User Service using the provided JWT token.
        This verifies that the user exists and the token is authorized.
        """
        async with httpx.AsyncClient() as client:
            try:
                # We call the user service to get the user based on the token context
                # The token passed here must have adequate permissions to fetch the user_id
                response = await client.get(
                    f"{settings.USER_SERVICE_URL}/api/v1/users/user/{user_id}",
                    headers={"Authorization": f"Bearer {token}"}
                )
                
                if response.status_code == 200:
                    json_resp = response.json()
                    # Extract the payload from the newly added custom response wrapper
                    return json_resp.get("data", json_resp)
                elif response.status_code == 404:
                    raise HTTPException(status_code=404, detail="User not found in User Service")
                elif response.status_code == 403:
                    raise HTTPException(status_code=403, detail="Not authorized to fetch this user info")
                else:
                    raise HTTPException(status_code=response.status_code, detail="Error communicating with User Service")
                    
            except httpx.RequestError as exc:
                raise HTTPException(status_code=503, detail=f"User Service is unavailable: {exc}")
