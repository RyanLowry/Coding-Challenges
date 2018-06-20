using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Text.RegularExpressions;

namespace DiceRoller
{
    class Program
    {

        //Add random outside of loop to widen random chances;
        public static Random rnd = new Random();
        static void Main(string[] args)
        {
            //regex for validation and to allow any number of dice rolls and sides;
            Regex regex = new Regex(@"\d+[d]\d+");
            string input = "";
            while(true)
            {

                Console.Write("Enter value in NdM formatting:");
                input = Console.ReadLine();
                if (regex.Match(input).Success)
                {
                    int[] output = RollDice(input);

                    Console.WriteLine("{0}: {1}", output.Sum(), string.Join(",", output));
                }else
                {
                    Console.WriteLine("Incorrect formatting, use NdM");
                }
            }

        }
        static int[] RollDice(string input)
        {
            
            int[] parse = parseData(input);
            int[] output = generateRolls(parse);
            return output;

        }
        static int[] parseData(string input)
        {
            int[] intData = Array.ConvertAll(input.Split('d'), int.Parse);
            return intData;
        }
        static int[] generateRolls (int[] parse)
        {
            //parse 0 = numDice, 1 = sides of dice
            int[] rollNumbers = new int[parse[0]];
            for (var i = 0; i < parse[0]; i++)
            {
                int rndNum = rnd.Next(1, parse[1]+1);
                rollNumbers[i] = rndNum;
            }
            return rollNumbers;
        }
    }
}