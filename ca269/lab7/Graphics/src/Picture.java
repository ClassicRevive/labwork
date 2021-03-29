/*
   This program uses the Mouse.

   Start the program and you will notice some objects drawn on the screen.
   When you click within any item, the outline changes to red.

   This is designed to show that polymorphism can be used to draw and select items.
*/
import java.awt.Graphics;
import java.awt.Color;
import javax.swing.JFrame;
import javax.swing.JPanel;

import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;

import java.util.List;
import java.util.ArrayList;

class Point
{
    private double x, y;

    public Point(double x, double y)
    {
        this.x = x;
        this.y = y;
    }
    public double getX() { return x; }
    public double getY() { return y; }

    public String toString() { return "Point(" + x + ", " + y + ")" ; }
}

abstract class Shape
{
    abstract void draw(Graphics g);
    abstract boolean contains(Point p);

}

class Circle extends Shape
{
    private int x, y, r;

    Circle(int x, int y, int r)
    {
        // Centre is at x,y
        this.x = x;
        this.y = y;
        // radius r
        this.r = r;
    }

    void draw(Graphics g)
    {
        // Java uses the drawOval class to draw a circle.
        // This draws an oval in a rectangle, so we need to work out
        // The rectangle (really square) which surrounds the circle
        g.drawOval(x - r, y - r, 2 * r, 2 * r);
    }

    // Is this point within the circle.
    boolean contains(Point p)
    {
        // Check if the distance from the centre to this point is less than the radius
        double xDist = x - p.getX();
        double yDist = y - p.getY();
        double distSquared = xDist * xDist + yDist * yDist;
        return distSquared < r * r;
    }

    public String toString() { return "Circle(" + x + ", " + y + ", " + r + ")" ; }
}

// class to draw rectangles
class Rect extends Shape
{
    private int x, y, width, height;

    Rect(int x, int y, int width, int height)
    {
        this.x = x;
        this.y = y;
        this.width = width;
        this.height = height;

    }

    // draw a rectangle
    void draw(Graphics g)
    {
        g.drawRect(x, y, width, height);
    }

    // check if a point is contained within a rectangle
    boolean contains(Point p)
    {
        // Check that x is not out of bounds and y not out of bounds
        return !(p.getX() < x || p.getX() > x + width || p.getY() < y || p.getY() > y + height);
    }

    // print out the rectangle
    public String toString() { return "Rect(" + x + ", " + y + ", " + width + ", " + height + ")" ; }
}

public class Picture extends JPanel implements MouseListener
{
    private List<Shape> shapes;
    private List<Shape> selected;

    public static void main(String[] a)
    {
        // Create the Frame (i.e. window)
        JFrame frame = new JFrame();

        Picture picture = new Picture();

        // Need to do this for any window ...
        frame.setSize(400, 400);
        frame.add(picture);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);

        // Create our shapes
        List<Shape> shapes = new ArrayList<Shape>();
        shapes.add(new Circle(0, 0, 30)); // One in the upper left corner
        shapes.add(new Circle(200, 200, 30)); // One in the centre

        shapes.add(new Rect(200 - 30, 200 - 30, 60, 60)); // Rectangle surrounding the circle

        // Add them to the picture
        picture.shapes = shapes;
        picture.selected = new ArrayList<Shape>();
        // Needed so we can respond to mouse clicks
        picture.addMouseListener(picture);
    }

    public void paint(Graphics g)
    {
        // First draw non selected shapes
        List<Shape> toDraw = new ArrayList<Shape>(shapes);
        toDraw.removeAll(selected);

        g.setColor (Color.blue);   // Set the colour ...
        for(Shape shape : toDraw)
            shape.draw(g);    // and draw any shapes

        // Now draw the selected shapes in Red
        g.setColor (Color.red);
        for(Shape shape : selected)
            shape.draw(g);
    }

    // Java calls this function when the mouse has been clicked.
    public void mouseClicked(MouseEvent e)
    {
        Point mouse = new Point(e.getX(), e.getY());

        // Clear the selected list
        selected.clear();
        for(Shape shape : shapes) // run through all shapes and see if any contain the mouse.
            if(shape.contains(mouse))
                selected.add(shape);

        // Tell Java to redraw the window
        this.repaint();
        this.revalidate();
    }

    // The following method definitions do nothing. They are required to implement the MouseListener interface.
    public void mouseExited(MouseEvent e) {}
    public void mouseEntered(MouseEvent e) {}
    public void mouseReleased(MouseEvent e) {}
    public void mousePressed(MouseEvent e) {}
}