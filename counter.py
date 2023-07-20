import tkinter as tk
from tkinter import ttk, messagebox


class CardCounter:
    def __init__(self, root):
        self.root = root
        self.card_values = {
            '2': 1,
            '3': 1,
            '4': 1,
            '5': 1,
            '6': 1,
            '7': 0,
            '8': 0,
            '9': 0,
            '10': -1,
            'J': -1,
            'Q': -1,
            'K': -1,
            'A': -1
        }
        self.running_count = 0
        self.total_decks = 1
        self.true_count = 0
        self.prev_card = None
        self.create_widgets()

    def create_widgets(self):
        self.root.title('Card Counter')
        self.root.geometry('800x200')

        self.deck_label = tk.Label(self.root, text='Number of Decks:')
        self.deck_label.grid(row=0, column=0, sticky='w')

        self.deck_combobox = ttk.Combobox(
            self.root, values=[i for i in range(1, 11)], state='readonly')
        self.deck_combobox.current(0)
        self.deck_combobox.grid(row=0, column=1, sticky='w')

        self.card_label = tk.Label(self.root, text='Cards:')
        self.card_label.grid(row=1, column=0, sticky='w')

        for i, card in enumerate(self.card_values.keys(), start=1):
            card_button = tk.Button(
                self.root, text=card, command=lambda card=card: self.update_count(card))
            card_button.grid(row=1, column=i)

        self.undo_button = tk.Button(
            self.root, text='Undo', command=self.undo_last_card)
        self.undo_button.grid(row=2, column=0)

        self.count_label = tk.Label(
            self.root, text='Running Count: 0\nTrue Count: 0')
        self.count_label.grid(row=3, column=0, columnspan=2)

        self.bet_advice_label = tk.Label(
            self.root, text='Bet Advice: Bet minimum')
        self.bet_advice_label.grid(row=4, column=0, columnspan=2)

    def calculate_true_count(self):
        try:
            return self.running_count / self.total_decks
        except ZeroDivisionError:
            return 0

    def update_count(self, card):
        self.total_decks = int(self.deck_combobox.get())
        self.deck_combobox.config(state='disabled')
        self.running_count += self.card_values[card]
        self.true_count = self.calculate_true_count()
        self.count_label.config(
            text=f'Running Count: {self.running_count}\nTrue Count: {self.true_count:.2f}')
        self.prev_card = card
        self.update_bet_advice()

    def undo_last_card(self):
        if self.prev_card:
            self.running_count -= self.card_values[self.prev_card]
            self.true_count = self.calculate_true_count()
            self.count_label.config(
                text=f'Running Count: {self.running_count}\nTrue Count: {self.true_count:.2f}')
            self.prev_card = None
            self.update_bet_advice()
        else:
            messagebox.showinfo('Info', 'No previous card to undo.')

    def update_bet_advice(self):
        if self.true_count > 2:
            advice = 'Increase your bet'
        elif self.true_count < 2:
            advice = 'Decrease your bet'
        else:
            advice = 'Bet with caution'
        self.bet_advice_label.config(text=f'Bet Advice: {advice}')


if __name__ == '__main__':
    root = tk.Tk()
    counter = CardCounter(root)
    root.mainloop()