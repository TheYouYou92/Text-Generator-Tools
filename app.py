from flask import Flask, render_template, request,redirect,flash
import text_analysis_tool, text_generator_tool, text_encryption_tool, text_formatter_tool, text_compare_tool,text_randomizer,text_summarizer_tool, text_spinner
import random
app = Flask(__name__)
app.secret_key = "dfsdfsdfsfsdfs"
@app.route('/')
def home():
    return render_template('home.html')


@app.route('/text_analysis', methods=['GET', 'POST'])
def text_analysis():
    if request.method == 'POST':
        text = request.form['text']
        analysis = text_analysis_tool.analyze(text)
        return render_template('text_analysis.html', analysis=analysis)
    return render_template('text_analysis.html')

@app.route('/text_encryption', methods=['GET', 'POST'])
def text_encryption():
    if request.method == 'POST':
        text = request.form['text']
        method = request.form['method']
        action = request.form['action']
        if action == 'encrypt':
            result = text_encryption_tool.encrypt(text, method)
        else: # action == 'decrypt'
            result = text_encryption_tool.decrypt(text, method)
        return render_template('text_encryption.html', result=result)
    return render_template('text_encryption.html')

@app.route('/text_generator', methods=['GET', 'POST'])
def text_generator():
    if request.method == 'POST':
        source = request.form['source']
        text = text_generator_tool.generate(source)
        return render_template('text_generator.html', text=text)
    return render_template('text_generator.html')

@app.route('/text_formatter', methods=['GET', 'POST'])
def text_formatter():
    if request.method == 'POST':
        text = request.form['text']
        format = request.form['format']
        action = request.form['action']
        formatted_text = text_formatter_tool.format(text, format, action)
        return render_template('text_formatter.html', formatted_text=formatted_text)
    return render_template('text_formatter.html')

@app.route('/text_compare', methods=['GET', 'POST'])
def text_compare():
    if request.method == 'POST':
        text1 = request.form['text1']
        text2 = request.form['text2']
        differences = text_compare_tool.compare(text1, text2)
        return render_template('text_compare.html', differences=differences)
    return render_template('text_compare.html')
@app.route('/text_summarizer', methods=['GET', 'POST'])
def text_summarizer():
    if request.method == 'POST':
        text = request.form['text']
        summary = text_summarizer_tool.summarize(text)
        return render_template('text_summarizer.html', summary=summary)
    return render_template('text_summarizer.html')
@app.route('/text_shuffler', methods=['GET', 'POST'])
def text_shuffler():
    if request.method == 'POST':
        text = request.form.get('text')
        try:
            shuffled_text = ''.join(random.sample(text, len(text)))
            return render_template('text_shuffler.html', shuffled_text=shuffled_text)
        except ValueError:
            return render_template('text_shuffler.html', error="Invalid input. Please enter a string.")
    return render_template('text_shuffler.html')

@app.route('/text_spinner', methods=['GET','POST'])
def spinner():
    if request.method == 'POST':
        input_text = request.form.get('text','')
        if input_text:
            
        
            spun_text = text_spinner.text_spinner(input_text)
            spinner = {"spun_text": spun_text}
            return render_template('text_spinner.html', spinner=spinner)
        else:
            # Flashing a message to the user
            flash("Please enter some text to spin.")

            # Redirecting the user back to the home page
            return redirect("/text_spinner")
    else:
        return render_template('text_spinner.html')
@app.route('/text_randomizer', methods=['GET', 'POST'])
def randomizer():
    if request.method == 'POST':
        input_text = request.form.get('text','')
        level = request.form['level']
        if input_text:
            randomize = text_randomizer.randomize_text(input_text, level)
            randomized = {'randomized':randomize}
            return render_template('/text_randomizer.html', randomized=randomized)
        else:
            flash('input text to randomize')
            return redirect('/text_randomizer')
    else:
        return render_template('/text_randomizer.html')
    
if __name__ == '__main__':
    app.run(debug=True)