"""
Text Processor Application
Student: Elsheikh Mohamed
ID: 1001486517 (Last Digits: 6517)
Date: November 3, 2025

Cloud Computing Assignment - Questions 10, 11, 12
"""

from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_q10', methods=['POST'])
def process_q10():
    """Question 10: Character counting, frequency, and replacement"""
    data = request.json
    S = data.get('S', '')
    T = data.get('T', '')
    C = data.get('C', '')
    operation = data.get('operation', '')
    
    results = {}
    
    if operation == 'count':
        char_counts = {}
        for char in S:
            char_counts[char] = T.count(char)
        results['counts'] = char_counts
        
    elif operation == 'frequency':
        total_chars = len(T)
        char_frequencies = {}
        for char in S:
            count = T.count(char)
            frequency = (count / total_chars * 100) if total_chars > 0 else 0
            char_frequencies[char] = {
                'count': count,
                'frequency': f"{frequency:.2f}%"
            }
        results['frequencies'] = char_frequencies
        
    elif operation == 'replace':
        modified_text = T
        replaced_count = 0
        for char in S:
            count = modified_text.count(char)
            replaced_count += count
            modified_text = modified_text.replace(char, C)
        results['modified_text'] = modified_text
        results['replaced_count'] = replaced_count
        results['original_text'] = T
    
    return jsonify(results)

@app.route('/process_q11', methods=['POST'])
def process_q11():
    """Question 11: Word counting and word listing by first character"""
    data = request.json
    S = data.get('S', '')
    T = data.get('T', '')
    operation = data.get('operation', '')
    
    results = {}
    words = re.findall(r'\b[a-zA-Z]+\b', T)
    
    if operation == 'count':
        results['word_count'] = len(words)
        results['words'] = words
        
    elif operation == 'list_by_char':
        words_by_char = {}
        for char in S:
            matching_words = [word for word in words if word.lower().startswith(char.lower())]
            words_by_char[char] = matching_words
        results['words_by_char'] = words_by_char
    
    return jsonify(results)

@app.route('/process_q12', methods=['POST'])
def process_q12():
    """Question 12: Remove stop words and show bi-grams"""
    data = request.json
    S = data.get('S', '')
    T = data.get('T', '')
    P = data.get('P', [])
    operation = data.get('operation', '')
    
    results = {}
    words = re.findall(r'\b[a-zA-Z]+\b', T)
    
    if operation == 'remove_stopwords':
        stop_words_lower = [word.lower() for word in P]
        filtered_words = []
        removed_count = 0
        
        for word in words:
            if word.lower() in stop_words_lower:
                removed_count += 1
            else:
                filtered_words.append(word)
        
        results['filtered_text'] = ' '.join(filtered_words)
        results['removed_count'] = removed_count
        results['original_text'] = ' '.join(words)
        results['filtered_words'] = filtered_words
        
    elif operation == 'bigrams':
        stop_words_lower = [word.lower() for word in P]
        filtered_words = [word for word in words if word.lower() not in stop_words_lower]
        
        bigrams = {}
        
        for i, word in enumerate(filtered_words):
            if any(word.lower().startswith(char.lower()) for char in S):
                word_bigrams = []
                
                if i > 0:
                    word_bigrams.append(f"{filtered_words[i-1]} {word}")
                
                if i < len(filtered_words) - 1:
                    word_bigrams.append(f"{word} {filtered_words[i+1]}")
                
                if word_bigrams:
                    if word not in bigrams:
                        bigrams[word] = []
                    bigrams[word].extend(word_bigrams)
        
        results['bigrams'] = bigrams
        results['filtered_words'] = filtered_words
    
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
