import time
import random

def typing_test():
    # List of sentences (can be expanded)
    sentences = [
        "Over 80% of Australia’s animals are found nowhere else on Earth",
        "Australia is the sixth-largest country in the world by land area",
        "The iconic Sydney Opera House is a UNESCO World Heritage Site",
        "Taronga Zoo in Sydney houses over 4,000 animals and offers harbour views",
        "The University of Sydney is Australia’s first university, founded in 1850",
        "University consistently ranks among the top 50 universities in the world",
        "Australia has three time zones and observes daylight saving in some regions",
        "Australia is the only continent that is also a country"
    ]
    
    used_sentences = []  # Track used sentences
    
    while True:
        # Get a new random sentence not used in this session
        available_sentences = [s for s in sentences if s not in used_sentences]
        if not available_sentences:  # If all sentences used
            available_sentences = sentences.copy()
            used_sentences = []
        
        sentence = random.choice(available_sentences)
        used_sentences.append(sentence)
        
        print("\n" + "="*40)
        print("Typing Speed Test")
        print("="*40)
        print(f"\nType this: '{sentence}'\n")
        
        input("Press Enter when ready to start...")
        print("\nGO!\n")
        
        start_time = time.time()
        user_input = input("Start typing: ")
        end_time = time.time()
        
        # Calculate results
        time_taken = end_time - start_time
        correct = 0
        total_chars = min(len(sentence), len(user_input))
        
        for i in range(total_chars):
            if sentence[i] == user_input[i]:
                correct += 1
        
        # Calculate WPM (5 chars = 1 word)
        words = correct / 5
        minutes = time_taken / 60
        wpm = words / minutes if minutes > 0 else 0
        accuracy = (correct / len(sentence)) * 100 if len(sentence) > 0 else 0
        
        # Display results
        print("\n" + "="*40)
        print("Your Results:")
        print(f"Time: {time_taken:.2f} seconds")
        print(f"Speed: {wpm:.1f} WPM")
        print(f"Accuracy: {accuracy:.1f}%")
        
        # Show mistakes
        if user_input != sentence:
            print("\nMistakes:")
            for i in range(total_chars):
                if sentence[i] != user_input[i]:
                    print(f"Position {i+1}: Expected '{sentence[i]}', got '{user_input[i]}'")
        
        # Ask to play again
        choice = input("\nTry again? (y/n): ").lower()
        if choice != 'y':
            print("\nThanks for playing!")
            break

# Start the test
typing_test()
