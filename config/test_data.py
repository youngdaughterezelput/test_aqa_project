from pydantic import BaseModel, Field


class LoginUser(BaseModel):
    username: str
    password: str


class UiElementCollection(BaseModel):
    name: str
    class_name: str
    minimum_count: int = Field(ge=1)


class VisibleUiElementExpectation(BaseModel):
    name: str
    selector_type: str
    selector_value: str
    minimum_count: int = Field(default=1, ge=1)


class PresentUiElementExpectation(BaseModel):
    name: str
    selector_type: str
    selector_value: str
    minimum_count: int = Field(default=1, ge=1)


admin_user = LoginUser(
    username="Admin",
    password="admin123",
)


login_social_icons = UiElementCollection(
    name="Login social icons",
    class_name="oxd-icon orangehrm-sm-icon",
    minimum_count=4,
)


login_branding_container = VisibleUiElementExpectation(
    name="Login branding container",
    selector_type="class",
    selector_value="orangehrm-login-branding",
)


login_branding_logo = PresentUiElementExpectation(
    name="OrangeHRM logo image",
    selector_type="css",
    selector_value='img[alt="orangehrm-logo"]',
)
