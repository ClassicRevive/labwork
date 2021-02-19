public class Word {
    public static boolean isFirstLetter(String word, char letter) {
        return word.charAt(0) == letter;
    }

    public static boolean containsLetter(String word, char letter) {
        boolean found = false;
        for (int i = 0; i < word.length(); i++)
        {
            if (word.charAt(i) == letter)
            {
                found = true;
                break;
            }
        }
        return found;
    }

    // replace a character in word with placeholder "0"
    public static String replace(String word, char c)
    {
        int i = 0;

        // linear search for character
        while (i < word.length()) {
            if (word.charAt(i) == c)  // replace with 0
                word = word.substring(0, i) + "0" + word.substring(i + 1);
            i++;
        }

        return word;
    }

    public static boolean allDone(String word, String guess)
    {
        String testWord = word;
        // create 0-string to check success condition
        String dummy = "";
        for (int i=0; i<word.length(); i++)
            dummy += "0";

        // loop through the guess characters.
        for (int i=0; i<guess.length(); i++) {
            // if we have a match, modify test word and keep checking
            char g = guess.charAt(i);
            if (containsLetter(testWord, g))
                testWord = replace(testWord, g);
        }

        return testWord.equals(dummy);
    }

    public static boolean allDone2(String word, String guess)
    {
        int count = 0;
        for (int i=0; i < word.length(); i++)
        {
            if (containsLetter(guess, word.charAt(i)))
                count++;
        }
        return count == word.length();
    }

    public static String showLetter(String word, char guess)
    {
        char [] array = new char [word.length()];
        for (int i=0; i < word.length(); i++)
        {
            if (word.charAt(i) == guess)
                array[i] = guess;
            else
                array[i] = '_';
        }
        return new String(array);
    }


    public static String showLetters(String word, String guesses)
    {
        char [] array = new char [word.length()];

        // fill array with underscores first
        for (int i=0; i<word.length(); i++) {
            array[i] = '_';
        }

        // for each letter in guess, loop through word
        for (int i = 0; i < guesses.length(); i++)
        {
            for (int j = 0; j < word.length(); j++)
            {
                if (guesses.charAt(i) == word.charAt(j))
                    array[j] = guesses.charAt(i);

            }
        }
        return new String(array);
    }

    public static String getRandomWord()
    {
        // Start with an array of words ... if you want more words, simply add to this list.
        String [] words = {
                "funny",
                "money",
                "stylish",
                "show",
                "toy",
                "code",
                "computer",
                "int",
                "teddy",
                "while",
        };

        // Choose one of these words randomly ...
        // ... Need a random index between 0 and words.length
        int randomIndex = (int) (Math.random() * words.length);

        // Use the index to return one of these words.
        return words[randomIndex];
    }

    public static void main(String [] args)
    {
        System.out.println("word: baad");
        System.out.println(allDone2("baad", "abcdefghijklmnopqrstuvwxyz"));
        System.out.println("word: baad, guess: b");
        System.out.println(showLetter("baad", 'b'));
        System.out.println(showLetters("baad", "ba"));


    }
}