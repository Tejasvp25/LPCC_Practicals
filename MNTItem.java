public class MNTItem{
	String macro_name;
	int mdt_pointer;
	
	MNTItem(String macro_name,int mdt_pointer){
		this.macro_name = macro_name;
		this.mdt_pointer = mdt_pointer;
	}
	
	public String toString() {
		return macro_name + " " + String.valueOf(mdt_pointer);
	}
	
}