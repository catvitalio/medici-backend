from faststream.rabbit import RabbitRouter

from dtos.jwt import TokenPairDTO

router = RabbitRouter()


@router.subscriber('user.login.command')
@router.publisher('user.logged_in.event')
async def login() -> TokenPairDTO:
    return TokenPairDTO(access='access', refresh='refresh')
