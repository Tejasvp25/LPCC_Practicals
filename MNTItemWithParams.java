
public class MNTItemWithParams {
	String macro_name;
	int mdt_pointer,noOfParams;
	
	MNTItemWithParams(String macro_name,int mdt_pointer,int noOfParams){
		this.macro_name = macro_name;
		this.mdt_pointer = mdt_pointer;
		this.noOfParams = noOfParams;
	}
	
	public String toString() {
		return macro_name + " " + String.valueOf(mdt_pointer) + " " + noOfParams;
	}
	
}
