import random

class MillionaireGame:
    def __init__(self):
        self.questions = [
            {"question": "Które polskie miasto jest znane z Królewskiego Zamku na Wawelu?", "options": ["1. Warszawa", "2. Gdańsk", "3. Berlin", "4. Kraków"], "answer": "4"},
            {"question": "W którym roku Polska odzyskała niepodległość?", "options": ["1. 1918", "2. 1946", "3. 1774", "4. 1880"], "answer": "1"},
            {"question": "Jak nazywa się najwyższy szczyt Tatr polskich?", "options": ["1. Rysy", "2. Giewont", "3. Kasprowy Wierch", "4. Śnieżka"], "answer": "1"},
            {"question": "Co oznacza skrót NASA", "options":["1.North American Space Association", "2.Nordic Aeronautic and Space Agency", "3.National Aeronautics and Space Administration", "4.Nordic Aeronautic and Space Agency"], "answer": "3" },
            {"question": "Jaki zespół uważany jest za królów K-popu i wydał hit Dynamite, który stał się pierwszym koreańskim utworem na szczycie listy Billboard Hot 100", "options": ["1. EXO", "2. BLACKPINK", "3. BTS", "4. TWICE"], "answer": "3"},
            {"question": "Jak nazywa się największy ocean na Ziemi?", "options": ["1. Ocean Atlantycki", "2. Ocean Arktyczny", "3. Ocean Spokojny", "4. Ocean Indyjski"], "answer" : "3"},
        ]
        random.shuffle(self.questions)
        
        self.current_question_index = 0
        self.prize_money = [
            "$100", "$200", "$300", "$500", "$1,000", "$2,000", "$4,000", "$8,000", "$16,000", "$32,000",
            "$64,000", "$125,000", "$250,000", "$500,000", "$1,000,000"
        ]
        self.player_money = 0
        self.hints_available = {"50-50": True, "zadzwoń": True, "zapytaj": True}
        self.player_name = ""
        self.leaderboard = []
        x = set(self.hints_available)
        print(x)



    def display_question(self):
        question_data = self.questions[self.current_question_index]
        print(f"\nQuestion {self.current_question_index + 1}: {question_data['question']}")
        for option in question_data['options']:
            print(option)

    def get_user_answer(self):
        return input("Twoja odpowiedż (1, 2, 3, or 4): ").upper()

    def check_answer(self, user_answer):
        question_data = self.questions[self.current_question_index]
        correct_answer = question_data['answer']
        if user_answer == correct_answer:
            print("Correct!")
            self.player_money = self.prize_money[self.current_question_index]
        else:
            print(f"Wrong! Prawidłowa odpowiedź była {correct_answer}. Otrymasz ${self.player_money}.")
            self.update_leaderboard()
            self.end_game()

    def update_leaderboard(self):
        self.leaderboard.append({"name": self.player_name, "money": self.player_money})
        self.leaderboard = sorted(self.leaderboard, key=lambda x: int(x["money"].replace("$", "")), reverse=True)[:10]

    def display_leaderboard(self):
        print("\nLeaderboard:")
        for idx, entry in enumerate(self.leaderboard, start=1):
            print(f"{idx}. {entry['name']} - {entry['money']}")

    def end_game(self):
        print("\nKoniec!")
        self.display_leaderboard()
        play_again = input("Czy chcesz zagrać ponownie? (Tak/Nie): ").lower()
        if play_again == "Tak":
            self.reset_game()
            self.start_game()
        else:
            exit()

    def reset_game(self):
        self.current_question_index = 0
        self.player_money = 0
        self.hints_available = {"50-50": True, "zadzwoń": True, "zapytaj": True}
        self.player_name = ""

    def start_game(self):
        print("Witamy w Kto chce zostać milionerem!")
        self.player_name = input("Wpisz swoje imię: ")
        
        while self.current_question_index < len(self.questions):
            self.display_question()
            user_answer = self.get_user_answer()
            self.check_answer(user_answer)
            self.current_question_index += 1

        print(f"Witamy, {self.player_name}! Otrzymnasz ${self.player_money} i zostaniesz milionerem!")
        self.update_leaderboard()
        self.display_leaderboard()
        self.end_game()

if __name__ == "__main__":
    game = MillionaireGame()
    game.start_game()