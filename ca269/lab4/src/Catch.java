public class Catch {
    public static void main(String[] args) {
        Broken broke = new Broken();

        System.out.println("Testing");
        try {
            broke.cracked();
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("ArrayIndexOutOfBoundsException");
        } catch (ArithmeticException e){
            System.out.println("ArithmeticException");
        } catch (NullPointerException e){
            System.out.println("NullPointerException");
        }
        finally {
            System.out.println("Finally");
        }
    }
}