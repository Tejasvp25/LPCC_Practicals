import java.util.ArrayList;

public class Params {
	ArrayList<String> params;
	String macroName;
	
	Params(ArrayList<String> params,String macroName){
		this.macroName = macroName;
		this.params = params;
	}
	
	public String toString() {
		StringBuilder sb = new StringBuilder();
		sb.append("\n**"+macroName+"**\n");
		for(int i = 0;i < params.size() ; i++) {
			sb.append(params.get(i).replaceAll("&", "")+" -> " + "#" + String.valueOf(i) + "\n");
		}
		return sb.toString();
	}
}
