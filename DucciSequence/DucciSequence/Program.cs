using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DucciSequence
{
    // Program that logs out number of steps for values to all equal zero or a repeating pattern.
    // https://www.reddit.com/r/dailyprogrammer/comments/8sjcl0/20180620_challenge_364_intermediate_the_ducci/
    class Program
    {
        static void Main(string[] args)
        {
            string input = "";
            while (true)
            {
                Console.Write("Enter values seperated by commas:");
                input = Console.ReadLine();
                try
                {
                    List<int> lst = Array.ConvertAll(input.Split(','), s => int.Parse(s)).OfType<int>().ToList();
                    int numIter = Ducci(lst);
                    Console.WriteLine(numIter + " iterations");
                }
                catch(Exception e)
                {
                    Console.WriteLine("error:" + e);
                    Console.WriteLine("seperate input by commas");
                }

            }
        }

        static int Ducci(List<int> firstList)
        {

            List<List<int>> wholeList = new List<List<int>>();
            int iterations = 0;
            while (true)
            {
                List<int> list = new List<int>();
                iterations++;
                
                int firstItem = firstList[0];
                for (var i = 0; i < firstList.Count; i++)
                {
                    if (firstList.Count - 1 == i)
                    {
                        int newValue = Math.Abs(firstList[i] - firstItem);

                        list.Add(newValue);
                    }
                    else
                    {
                        int newValue = Math.Abs(firstList[i] - firstList[i + 1]);

                        list.Add(newValue);
                    }
                   
                }
                Console.WriteLine(string.Join(",", list));
                if (firstList.All(i => i == 0))
                {
                    return iterations;
                }
                else if (wholeList.Any(i => i.SequenceEqual(list)))
                {
                    return iterations + 1;
                }
                wholeList.Add(list);
                firstList = list;


            }
            
            
        }
    }
}
