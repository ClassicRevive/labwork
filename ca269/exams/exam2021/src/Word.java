public class Word {
    public static int howManyCorrect(String word, String guesses)
    {
        int count = 0;
        for (int i=0; i<word.length(); i++)
        {
            if (guesses.indexOf(word.charAt(i)) != -1)
            {
                count += 1;
            }
        }

        return count;
    }
}
