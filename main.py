from flask import Flask, render_template, request, flash, redirect, url_for
import random
import pandas as pd

app = Flask(__name__)

players = []


@app.route('/', methods=['GET', 'POST'])
def home():
  if request.method == 'POST':
    action = request.form.get('action')

    if action == 'add_player':
      player_name = request.form.get('player_name')
      if player_name != "":
        players.append(player_name)
        flash('Le joueur a été ajouté avec succès.', 'success')
      else:
        flash('Veuillez entrer un nom de joueur.', 'error')

    elif action == 'remove_player':
      player_name = request.form.get('player_name')
      if player_name in players:
        players.remove(player_name)
        flash('Le joueur a été supprimé avec succès.', 'success')
      else:
        flash('Le joueur spécifié n\'existe pas.', 'error')

    elif action == 'select_winner':
      num_winners = int(request.form.get('num_winners'))
      num_draws = int(request.form.get('num_draws'))
      draw_name = request.form.get('draw_name')

      if num_winners <= len(players):
        winners = []
        for _ in range(num_draws):
          selected_winners = random.sample(players, num_winners)
          winners.extend(selected_winners)

        flash(f'Gagnants : {", ".join(winners)}', 'success')
        return redirect(url_for('home'))

      else:
        flash(
          'Le nombre de gagnants spécifié est supérieur au nombre de joueurs.',
          'error')

  return render_template('index.html', players=players)

  return redirect(url_for('home'))


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)
