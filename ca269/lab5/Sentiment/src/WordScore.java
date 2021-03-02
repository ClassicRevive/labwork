public class WordScore
{
    String word;
    int score;

    public WordScore(String w)
    {
        word = w;
    }

    public int score(String review)
    {
        String [] tokens = review.split(" ");
        for (String token: tokens)
        {
            if (token.equals(word))
            {
                return Integer.parseInt(tokens[0]);
            }
        }
        return -1;
    }
}
