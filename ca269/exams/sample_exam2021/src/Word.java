public class Word {
    // Word.showLetters("computing", "gpo");
    // >> _o_p____g

    public static String showLetters(String word, String guesses)
    {
        StringBuilder newWord = new StringBuilder();
        for (int i=0; i < word.length() ; i++)
        {
            // if letter of word is contained in guesses
            if (guesses.indexOf(word.charAt(i)) != -1)
            {
                newWord.append(word.charAt(i));
            }
            else
            {
                newWord.append("_");
            }
        }
        return newWord.toString();
    }
}
