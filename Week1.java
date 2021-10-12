import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;

public class Week1 {
	
	ArrayList<String> MDT;
	ArrayList<MNTItem> MNT;
	
	String inputFileName = "samplew1.txt";
	String outputFileName = "outputw1.txt";
	
	File inputFile,outputFile;
	
	BufferedReader bufferedReader;
	BufferedWriter bufferedWriter;
	
	FileReader fReader;
	FileWriter fWriter;
	
	Week1(){
		MDT = new ArrayList<String>();
		MNT = new ArrayList<MNTItem>();
		inputFile = new File(inputFileName);
		outputFile = new File(outputFileName);
		
		try {
			fReader = new FileReader(inputFile);
			fWriter = new FileWriter(outputFile);
			bufferedReader = new BufferedReader(fReader);
			bufferedWriter = new BufferedWriter(fWriter);
			process();
			printOutput();
		} catch (Exception e) {
			System.out.println(e.getMessage());
		}		
	}

	void process() throws Exception {
		String line;
		while((line=bufferedReader.readLine())!=null)  
		{  
			if(line.contains("MACRO")) {
				MNT.add(new MNTItem(line.split(" ")[1],MDT.size()));
				processMDT();
			}else {
				bufferedWriter.write(line + "\n");
			}
		}
		bufferedWriter.flush();
		fWriter.close();
		fReader.close();
	}
	
	void processMDT() throws Exception {
		String line;
		while((line=bufferedReader.readLine())!=null)  
		{  
			MDT.add(line);
			if(line.contains("MEND")) {
				break;
			}
		}
//		line=bufferedReader.readLine();
//		bufferedWriter.write(line + "\n");
	}
	
	void printOutput(){
		int i;
		System.out.println("**MDT**");
		for(i = 0; i < MDT.size(); i++) {
			System.out.println(MDT.get(i));
		}
		System.out.println();
		System.out.println("**MNT**");
		for(i = 0; i < MNT.size(); i++) {
			System.out.println(MNT.get(i).toString());
		}
		System.out.println();
	}
	
	public static void main(String[] args) {
		new Week1();
	}

}

