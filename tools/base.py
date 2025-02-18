from kubiya_sdk.tools import Tool
from kubiya_sdk.tools.registry import tool_registry

# Constants should be at the top and use UPPERCASE
KUBERNETES_ICON_URL = "https://storage.getlatka.com/images/kubiya.ai.png"
API_ENDPOINT = "https://api.kubiya.ai/api/v1/onboard"

# Tool definition with improved formatting and structure
onboarding_mate = Tool(
    name="onboarding_mate",
    description="Onboard a new organization to Kubiya",
    image="alpine/curl",
    content=f"""curl -X POST {API_ENDPOINT} \
  -H "Authorization: UserKey ${{KUBIYA_API_KEY}}" \
  -H "Content-Type: application/json" \
  -d '{{
    "org_name": "'"${{org_name}}"'",
    "admin_email": "'"${{admin_email}}"'"
  }}'""",
    secrets=["KUBIYA_API_KEY"],
    args=[
        {
            "name": "org_name",
            "description": "The name of the organization",
            "type": "str",
            "required": True,
        },
        {
            "name": "admin_email",
            "description": "The email of the organization admin",
            "type": "str",
            "required": True,
        },
    ],
)

# Register the tool
tool_registry.register("onboarding_mate", onboarding_mate)