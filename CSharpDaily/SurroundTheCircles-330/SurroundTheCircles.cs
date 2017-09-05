using System;
using System.Collections.Generic;

namespace SurroundTheCircles_330
{
    public class SurroundTheCircles
    {
        
        public static void Main(string[] args)
        {
            System.Globalization.CultureInfo customCulture = (System.Globalization.CultureInfo)System.Threading.Thread.CurrentThread.CurrentCulture.Clone();
            customCulture.NumberFormat.NumberDecimalSeparator = ".";
            System.Threading.Thread.CurrentThread.CurrentCulture = customCulture;
            HashSet<Circle> circles = new HashSet<Circle>();
            string circle;
            Console.WriteLine("Enter a circle per line 'x,y,r'");
            while (!string.IsNullOrWhiteSpace(circle = Console.ReadLine()))
            {
                string[] parse = circle.Split(',');
                circles.Add(new Circle(Int32.Parse(parse[0]), Int32.Parse(parse[1]), Convert.ToDouble(parse[2])));
            }
            Console.WriteLine("These are the circles you entered");
            foreach(Circle cir in circles)
            {
                Console.Write(cir.ToString()); //TODO doesnt use overwritten ToString function
            }
            Console.Write('\n');

            double hx = 0, lx = 0, hy = 0, ly = 0;
            foreach (Circle cir in circles)
            {
                if (cir.x + cir.r > hx)
                    hx = cir.x + cir.r;
                if (cir.x - cir.r < lx)
                    lx = cir.x - cir.r;
                if (cir.y + cir.r > hy)
                    hy = cir.y + cir.r;
                if (cir.y - cir.r < ly)
                    ly = cir.y - cir.r;
            }
            Console.WriteLine(string.Format("({0:C2},{1:C2}), ({2:C2}, {3:C2}), ({4:C2}, {5:C2}), ({6:C2}, {7:C2})", lx, hy, hx, hy, hx, ly, lx, ly)); //TODO format to 3 decimal signed numbers without dollar signs
        }

        private class Circle
        {
            public int x, y;
            public double r;

            public Circle(int x, int y, double r)
            {
                this.x = x;
                this.y = y;
                this.r = r;
            }

            new string ToString()
            {
                return string.Format("{0},{1},{2} ", this.x, this.y, this.r);
            }
        }
    }
}