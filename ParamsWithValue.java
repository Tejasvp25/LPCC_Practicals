import java.util.ArrayList;

public class ParamsWithValue extends Params {

	ArrayList<String> values;
	
	ParamsWithValue(ArrayList<String> params, ArrayList<String> values,String macroName) {
		super(params, macroName);
		this.values = values;
	}
	
	public String toString() {
		StringBuilder sb = new StringBuilder();
		sb.append("\n**"+macroName+"**\n");
		for(int i = 0;i < params.size() ; i++) {
			sb.append("#" + String.valueOf(i)+" -> "+ values.get(i));
		}
		return sb.toString();
	}
}
