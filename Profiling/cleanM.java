import java.io.IOException;
import org.apache.hadoop.io.NullWritable;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class cleanM
    extends Mapper<LongWritable, Text, NullWritable, Text> 
{
    @Override
	public void map(LongWritable key, Text value, Context context)
	throws IOException, InterruptedException 
	{    
	    String line = value.toString();
	    String delims = "[,]";

	    String[] tokens = line.split(delims);
	    String out = "";

	    for (int i = 0; i < tokens.length; i++)
		{
		    if ((i == 39)||(i == 202)||(i == 264)||(i == 265)||(i == 477)||(i == 478)||(i == 330)||(i == 385)||(i == 442)||(i == 203)||(i == 223)||(i == 267)||(i == 268)||(i == 270)||(i == 285)||(i == 277)||(i == 302)||(i == 408)||(i == 334)||(i == 519))
			{
			    out = out + tokens[i] + ",";
			}
		}
	    context.write(null, new Text(out));
	}
}