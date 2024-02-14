import autogen
from autogen.agentchat.contrib.retrieve_assistant_agent import RetrieveAssistantAgent
from autogen.agentchat.contrib.retrieve_user_proxy_agent import RetrieveUserProxyAgent
config_list = [
    {
          
        'api_type': 'open_ai',
        'api_base': 'http://localhost:1234/v1',
        'api_key': 'NULL'
    }
]

llm_config={
    "request_timeout": 600,
    "seed": 42,
    "config_list": config_list,
    "temperature": 0
}
assistant = RetrieveAssistantAgent(
    name="assistant",
    system_message="You are a helpful assistant and tech support trying to help people to understand the project by the documentation that is provided to you in context.",
    llm_config=llm_config,
)

ragproxyagent = RetrieveUserProxyAgent(
    name="ragproxyagent",
    retrieve_config={
        "task": "qa",
        "docs_path": "C:/Users/adity/rag/rprt.pdf",
    },
)
assistant.reset()
ragproxyagent.initiate_chat(assistant, problem="What are the weaknesses in this project")
