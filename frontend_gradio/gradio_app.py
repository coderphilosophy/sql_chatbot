import gradio as gr
from backend.orchestrator import ask

view = gr.ChatInterface(
    fn=ask,
    title="AI SQL Chat Assistant",
    description="Ask questions. DB queries will be answered; missing data triggers helpful fallbacks."
)

if __name__ == "__main__":
    view.launch(debug=True)
