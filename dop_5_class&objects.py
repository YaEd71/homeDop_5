class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __repr__(self):
        return f"User(nickname={self.nickname}, age={self.age})"


class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __repr__(self):
        return f"Video(title={self.title}, duration={self.duration}, adult_mode={self.adult_mode})"


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, login, password):
        for user in self.users:
            if user.nickname == login and user.password == password:
                self.current_user = user
                return
        print("Не верный логин или пароль")

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f"User {nickname} already exists")
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user

    def log_out(self):
        self.current_user = None

    def add(self, *videos):
        for video in videos:
            if not any(v.title == video.title for v in self.videos):
                self.videos.append(video)

    def get_videos(self, search_word):
        search_word = search_word.lower()
        return [video.title for video in self.videos if search_word in video.title.lower()]

    def watch_video(self, title):
        if not self.current_user:
            print("Войдите в аккаунт чтобы смотреть видео")
            return

        for video in self.videos:
            if video.title == title:
                if video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    return

                for second in range(video.time_now + 1, video.duration + 1):
                    print(second, end=" ", flush=True)
                print("Конец видео")
                video.time_now = 0
                return

        print("Видео не найдено")


# Test code
ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Adding videos
ur.add(v1, v2)

# Search test
print(ur.get_videos('Лучший'))
print(ur.get_videos('ПРОГ'))

# Login and age restriction test
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Test login with another account
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Attempt to watch a non-existent video
ur.watch_video('Лучший язык программирования 2024 года!')