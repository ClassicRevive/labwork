public class Word {

    public static String showLetters(String word, String guesses)
    {
        StringBuilder ans = new StringBuilder();

        for (int i=0; i<word.length(); i++)
        {
            if (guesses.indexOf(word.charAt(i)) != -1)
            {
                ans.append(word.charAt(i));
            }
            else
            {
                ans.append("_");
            }
        }
        return ans.toString();
    }
}
