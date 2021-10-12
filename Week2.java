import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;

public class Week2 {
	
	ArrayList<String> MDT;
	ArrayList<MNTItem> MNT;
	
	String inputFileName = "samplew2.txt";
	String outputFileName = "outputw2.txt";
	
	File inputFile,outputFile;
	
	BufferedReader bufferedReader;
	BufferedWriter bufferedWriter;
	
	FileReader fReader;
	FileWriter fWriter;
	
	Week2(){
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
				processMDT(line);
			}else {
				bufferedWriter.write(line + "\n");
			}
		}
		bufferedWriter.flush();
		fWriter.close();
		fReader.close();
	}
	
	void processMDT(String macroLine) throws Exception {
		int i;
		int index;
		String []splited = macroLine.replaceAll("MACRO ", "").replaceAll(",", " ").split(" ");
		MDT.add(String.join(" ", splited));
		String line;
		ArrayList<String> parameters = new ArrayList<String>();
		
		for(i = 0; i < splited.length; i++) {
			if(splited[i].contains("=")) {
				parameters.add(splited[i].split("=")[0]);
				continue;
			}
			parameters.add(splited[i]);
		}
		
		while((line=bufferedReader.readLine())!=null)  
		{  
			splited = line.replaceAll(",", " ").split(" ");
			line = "";
			for(i = 0; i < splited.length; i++) {
				if((index = parameters.indexOf(splited[i])) != -1) {
					splited[i] = "#"+String.valueOf(index-1);
				}
				line += " "+splited[i];
			}
			
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
		new Week2();
	}

}


