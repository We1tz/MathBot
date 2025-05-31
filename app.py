import asyncio
import re
from html import escape
from flask import Flask, render_template, request
from Model.model import ai_chat

app = Flask(__name__)

HTML_STYLES = """
    body {
        font-family: Arial, sans-serif;
        max-width: 800px;
        margin: 20px auto;
        line-height: 1.6;
    }
    h1, h2, h3 {
        margin-top: 1.2em;
        margin-bottom: 0.5em;
    }
    ol {
        padding-left: 1.2em;
    }
    .math-block {
        text-align: center;
        margin: 20px 0;
    }
"""

def format_result_with_latex(result: str) -> str:
    result = re.sub(r'\*+', '', result)
    segments = re.split(r'(\$\$.*?\$\$|\$.*?\$)', result, flags=re.DOTALL)
    formatted_segments = []

    for segment in segments:
        if segment.startswith('$$') and segment.endswith('$$'):
            formatted_segments.append(f'<div class="math-block">{segment}</div>')
        elif segment.startswith('$') and segment.endswith('$'):
            formatted_segments.append(segment)
        else:
            escaped_text = escape(segment).strip()
            if escaped_text:
                steps = re.split(r'(\d+\.\s)', escaped_text)
                formatted_text = ''
                i = 0
                while i < len(steps):
                    if re.match(r'\d+\.\s', steps[i]):
                        step_text = steps[i + 1].strip() if i + 1 < len(steps) else ''
                        formatted_text += f'<li>{step_text}</li>'
                        i += 2
                    else:
                        paragraph = steps[i].strip()
                        if paragraph:
                            formatted_text += f'<p>{paragraph}</p>'
                        i += 1
                if '<li>' in formatted_text:
                    formatted_segments.append(f'<ol>{formatted_text}</ol>')
                else:
                    formatted_segments.append(formatted_text)
    return ''.join(formatted_segments)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form.get('task')
        result = asyncio.run(ai_chat(user_input))
        formatted_result = format_result_with_latex(result)
        return render_template('result.html', result=formatted_result, styles=HTML_STYLES)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)