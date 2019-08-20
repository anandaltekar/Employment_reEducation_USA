import java.io.IOException;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class profileM
    extends Mapper<LongWritable, Text, Text, Text> 
{
    @Override
	public void map(LongWritable key, Text value, Context context)
	throws IOException, InterruptedException 
	{    
	    String line = value.toString();
	    String delims = "[,]+";

	    String[] tokens = line.split(delims);

	    long z = 0;
	    if (key.get() == z)
		{
		    for (int i = 0; i < tokens.length; i++)
			{
			    context.write(new Text(Integer.toString(i)), new Text("00H" + tokens[i]));
			}
		}
	    else
		{
		    for (int i = 0; i < tokens.length; i++)
			{
			    context.write(new Text(Integer.toString(i)), new Text(tokens[i]));
			}
		}
	}
}