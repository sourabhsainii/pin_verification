from model.pin_verify_request import PinVerifyRequest
from model.pin import Pin
from verifyPinService import verifyPinService

def verify_pin(
    request: PinVerifyRequest,
    context
) -> Pin:
    """Verifies a pin"""

    print("request:::::: ", request.body)

    pinService = verifyPinService()

    pinService.verifyPin(request.body)