using System;
 
namespace Sample
{
    class Sample
    {
        static void Main()
        {
            string str = "Hello World!";
            string target = "W";
            
            if(str.Contains(target)) {
                Console.WriteLine("{0}が見つかりました", target);    
            } else {
                Console.WriteLine("{0}は見つかりませんでした", target);
            }
            
            Console.ReadKey();
        }
    }
}
