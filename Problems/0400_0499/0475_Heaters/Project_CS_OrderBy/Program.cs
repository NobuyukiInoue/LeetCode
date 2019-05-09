using System.Collections;
using System.Collections.Generic;
using System.Linq;

namespace Project_CS_OrderBy
{
    public static class Program
    {
        static void Main( string[] args )
        {
            int[]       dataA   = new int[] { 3, 1, 2, 0, 4 };
            List<float> dataB   = new List<float>() { 1.5f, 1.3f, 3.2f };
            string[]    dataC   = new string[] { "正一郎", "清次郎", "誠三郎", "征史郎" };

            // 昇順に並べ替える
            IOrderedEnumerable<int>     orderedDataA    = dataA.OrderBy( value => value );
            IOrderedEnumerable<float>   orderedDataB    = dataB.OrderBy( value => value );
            IOrderedEnumerable<string>  orderedDataC    = dataC.OrderBy( value => value );

            System.Console.WriteLine( "dataA        :{0}", dataA.Text() );
            System.Console.WriteLine( "dataA ordered:{0}", orderedDataA.Text() );
            System.Console.WriteLine( "dataB        :{0}", dataB.Text() );
            System.Console.WriteLine( "dataB ordered:{0}", orderedDataB.Text() );
            System.Console.WriteLine( "dataC        :{0}", dataC.Text() );
            System.Console.WriteLine( "dataC ordered:{0}", orderedDataC.Text() );

            // 入力待ち用
            System.Console.ReadKey();
        }

        /// <summary>
        /// 簡易的なシーケンスのテキスト取得処理
        /// </summary>
        public static string Text( this IEnumerable i_source )
        {
            string text = string.Empty;
            foreach( var value in i_source )
            {
                text += string.Format( "[{0}], ", value );
            }
            return text;
        }

    } // class Program
}
