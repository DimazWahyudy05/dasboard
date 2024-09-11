from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    dashboard = conn.execute('SELECT * FROM dashboard ORDER BY id DESC LIMIT 1').fetchone()
    conn.close()
    return render_template('index.html', dashboard=dashboard)

@app.route('/update', methods=('GET', 'POST'))
def update():
    if request.method == 'POST':
        erdkk_urea = request.form['erdkk_urea']
        erdkk_npk_phonska = request.form['erdkk_npk_phonska']
        salur_urea = request.form['salur_urea']
        salur_phonska = request.form['salur_phonska']
        jumlah_petani = request.form['jumlah_petani']
        serapan_urea = request.form['serapan_urea']
        serapan_npk_phonska = request.form['serapan_npk_phonska']

        conn = get_db_connection()
        conn.execute('INSERT INTO dashboard (erdkk_urea, erdkk_npk_phonska, salur_urea, salur_phonska, jumlah_petani, serapan_urea, serapan_npk_phonska) VALUES (?, ?, ?, ?, ?, ?, ?)',
                     (erdkk_urea, erdkk_npk_phonska, salur_urea, salur_phonska, jumlah_petani, serapan_urea, serapan_npk_phonska))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))

    return render_template('form.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    