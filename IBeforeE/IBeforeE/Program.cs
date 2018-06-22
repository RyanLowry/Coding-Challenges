using System;
using System.IO;
using System.Net;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Text.RegularExpressions;

namespace IBeforeE
{
    /*
     * A program that detects if a word follows i before e except after c rule.
     * https://www.reddit.com/r/dailyprogrammer/comments/8q96da/20180611_challenge_363_easy_i_before_e_except/
     */

    class Program
    {
        static void Main(string[] args)
        {
            string input = "";
            
            while (true)
            {

                Console.Write("Enter any string or type 'read file' to read from a word list:");
                input = Console.ReadLine();
                if (input == "read file")
                {
                    Tuple<int,int> exc = readFile();
                    Console.WriteLine("there are {0} exceptions out of {1} total words",exc.Item1,exc.Item2);
                }
                else
                {
                    bool followsRule = FollowRule(input);
                    Console.WriteLine(followsRule);
                }



            }
            
        }
        static Tuple<int,int> readFile()
        {
            int exceptions = 0;
            int total = 0;
            try
            {
                using (WebClient client = new WebClient())
                using (Stream stream = client.OpenRead("https://norvig.com/ngrams/enable1.txt"))
                using (StreamReader reader = new StreamReader(stream))
                {
                    string line;
                    while ((line = reader.ReadLine()) != null)
                    {
                        bool rule = FollowRule(line);
                        if (rule == false)
                        {
                            exceptions++;
                        }
                        total++;
                        
                    }
                }
            }
            catch (Exception e)
            {
                Console.WriteLine("error:" + e);
            }
            return Tuple.Create(exceptions,total);
        }
        static bool FollowRule(string str)
        {
            bool withC = Regex.Match(str, @"cie").Success;
            bool withoutC = Regex.Match(str, @"[^c]ei").Success;
            //regex didn't detect ei at start of word, use startsWith to handle the exception;
            if (withC || withoutC || str.StartsWith("ei"))
            {
                return false;
            }
            return true;
        }
    }
}
