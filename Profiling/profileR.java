import java.io.IOException;
import java.util.*;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

public class profileR
    extends Reducer<Text, Text, Text, Text> 
{  
    @Override
	public void reduce(Text key, Iterable<Text> values, Context context)
	throws IOException, InterruptedException 
	{
	    int max = 0;
	    int min = 100;
	    String kee = "";
	    long wcount = 0;
	    List<String> wurds = new ArrayList<String>();
	    long num = 0;
	    long str = 0;
	    String type = "";

	    for (Text value : values) 
	    	{
		    String temp = value.toString();
		    if (temp.length() > 2)
			{
			    if (temp.substring(0, 3).matches("00H"))
				{
				    kee = temp;
				}
			    else
				{
				    int len = temp.length();
				    if (len > max)
					{
					    max = len;
					}
				    if (len < min)
					{
					    min = len;
					}
				    if (wurds.indexOf(temp) == -1)
					{
					    wurds.add(temp);
					    wcount++;
					}
				    if ((temp.length() >= 6) || (!temp.substring(0, 1).matches("\\d")))
					{
					    if (temp != "L")
						{
						    str++;
						}
					}
				    else if ((temp.length() <= 6) && (temp.substring(0, 1).matches("\\d")))
					{
					    num++;
					}
				}
			}
		    else
			{
			    int len = temp.length();
			    if (len > max)
				{
				    max = len;
				}
			    if (len < min)
				{
				    min = len;
				}
			    if (wurds.indexOf(temp) == -1)
				{
				    wurds.add(temp);
				    wcount++;
				}
			    if ((temp.length() >= 6) || (!temp.substring(0, 1).matches("\\d")))
				{
				    if (temp != "L")
					{
					    str++;
					}
				}
			    else if ((temp.length() <= 6) && (temp.substring(0, 1).matches("\\d")))
				{
				    num++;
				}
			}
	    	}    

	    if ((str == 0) && (num > 0))
		{
		    type = "int";
		}
	    else
		{
		    type = "String";
		}

	    String keymax = kee + " max";
	    String valmax = Integer.toString(max);
	    context.write(new Text(keymax), new Text(valmax));
	    String keymin = kee + " min";
	    String valmin = Integer.toString(min);
	    context.write(new Text(keymin), new Text(valmin));
	    String keywurd = kee + " words";
            String valword = Long.toString(wcount);
            context.write(new Text(keywurd), new Text(valword));
	    String keytype = kee + " type";
            String valtyp = type;
            context.write(new Text(keytype), new Text(valtyp));  
	}
}