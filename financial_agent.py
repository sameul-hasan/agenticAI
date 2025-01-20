from phi.agent import Agent
from phi.model.groq import Groq
from dotenv import load_dotenv
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools

load_dotenv()
agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
)

agent.print_response("Share a 2 sentence love story between dosa and samosa")