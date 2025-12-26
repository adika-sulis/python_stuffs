import time, os, random

def clearcls():
    os.system("cls" if os.name=="nt" else "clear")

clearcls()

sentences = [
    "The quick brown fox jumps over the lazy dog every morning",
    "Typing speed improves with daily practice and consistent focused effort",
    "She enjoys reading books while drinking coffee on rainy afternoons",
    "Learning Python can be fun, practical, and rewarding for many people",
    "The programmer fixed bugs quickly before the final deadline arrived",
    "A calm mind helps improve accuracy during fast typing exercises",
    "He writes code late at night when the house is quiet",
    "Small consistent improvements lead to impressive results over time",
    "The keyboard feels familiar after hours of repetitive typing practice",
    "Clear goals make learning new technical skills much easier",
    "They tested the application thoroughly before releasing it publicly",
    "Good posture helps prevent fatigue during long typing sessions",
    "Music can help some people maintain rhythm while typing quickly",
    "She practices typing every day to increase her words per minute",
    "Simple sentences are ideal for measuring raw typing speed accurately",
    "The screen displayed progress statistics after each completed test",
    "Focus on accuracy first, then gradually increase typing speed",
    "He challenged himself to beat his previous typing record today",
    "Warm-up exercises reduce errors during high speed typing tests",
    "The software records keystrokes to calculate accurate WPM results",
    "Typing without looking at the keyboard improves long term performance",
    "They created a minimal interface to avoid unnecessary distractions",
    "Regular breaks help maintain concentration and prevent mental fatigue",
    "Fast typing requires both muscle memory and focused attention",
    "She noticed fewer mistakes after slowing down her typing slightly",
    "The test includes random sentences to avoid memorization effects",
    "Consistent practice builds confidence and smoother typing flow",
    "He adjusted his chair height for better ergonomic comfort",
    "Clear text and good contrast improve readability during typing tests",
    "The application saves historical data to track long term improvement",
    "Typing accuracy matters more than speed in professional environments",
    "He prefers mechanical keyboards for better tactile feedback",
    "The lesson emphasized rhythm, precision, and relaxed hand movement",
    "They measured improvement after several weeks of daily practice",
    "Short sentences help beginners focus on basic typing mechanics",
    "The cursor blinked patiently, waiting for the next keystroke",
    "She smiled after seeing her highest WPM score so far",
    "The program highlights mistakes immediately to encourage correction",
    "Typing tests should feel challenging but not overly stressful",
    "He reset the test to try achieving a cleaner result",
    "Smooth typing feels almost automatic after enough repetition",
    "They compared results across different keyboards and layouts",
    "A quiet environment helps maintain consistent typing rhythm",
    "The test duration was long enough to ensure reliable results",
    "She focused on breathing steadily while typing at high speed",
    "The application loads instantly and responds without noticeable delay",
    "Daily repetition strengthens finger coordination and typing confidence",
    "He prefers short practice sessions spread throughout the day",
    "The final score reflected both speed and accuracy together",
    "Typing skills improve gradually through patience and disciplined practice"
]

phrase = random.choice(sentences)
print(f"Type the following sentence:        {phrase}")
input("Press enter to begin ")

start = time.time()
sentence = input("Type:    ").strip()
if sentence.lower() == phrase.lower():
    pass
elif sentence != phrase:
    print(f"You've made a mistake. Please try again!\nExpected: {phrase}\nReceived: {sentence}")
    exit()
end = time.time()
time_taken = (end - start)
wpm = len(phrase.split()) / time_taken
clearcls()
print(f"Time taken: {round(time_taken,2)}")
print(f"Estimated words per minute: {round(wpm*60,2)}")
