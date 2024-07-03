with open('american-english.txt', 'r') as f:
    content = f.read().splitlines()

    di = {item: len(item) for item in content}

    view = sorted(di.items(), key=lambda x: x[1], reverse=True)
    words_list = [word for word, length in view[:100]]
    
    print(words_list)
        
