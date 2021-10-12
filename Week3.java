import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;

public class Week3 {
	
	ArrayList<String> MDT;
	ArrayList<MNTItemWithParams> MNT;
	ArrayList<Params> paramList;
	ArrayList<String> macroNames;
	ArrayList<ParamsWithValue> paramsValue;
	
	String inputFileName = "samplew3.txt";
	String outputFileName = "outputw3.txt";
	
	File inputFile,outputFile;
	
	BufferedReader bufferedReader;
	BufferedWriter bufferedWriter;
	
	FileReader fReader;
	FileWriter fWriter;
	
	Week3(){
		MDT = new ArrayList<String>();
		MNT = new ArrayList<MNTItemWithParams>();
		paramList = new ArrayList<Params>();
		macroNames = new ArrayList<String>();
		paramsValue = new ArrayList<ParamsWithValue>();
		
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
		String macroName;
		while((line=bufferedReader.readLine())!=null)  
		{  
			if(line.contains("MACRO")) {
				macroName = line.split(" ")[1];
				MNT.add(new MNTItemWithParams(macroName,MDT.size(),line.replaceAll("MACRO ", "").replaceAll(",", " ").split(" ").length-1));
				macroNames.add(macroName);
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
//		MDT.add(String.join(" ", splited));
		
		String line;
		ArrayList<String> parameters = new ArrayList<String>();
		
		for(i = 1; i < splited.length; i++) {
			if(splited[i].contains("=")) {
				parameters.add(splited[i].split("=")[0]);
				continue;
			}
			parameters.add(splited[i]);
		}
		if(parameters.size() > 0)
			paramList.add(new Params(parameters,macroNames.get(macroNames.size()-1)));
		while((line=bufferedReader.readLine())!=null)  
		{  
			splited = line.replaceAll(",", " ").split(" ");
			line = "";
			for(i = 0; i < splited.length; i++) {
				if(isMacroCall(splited[i] )&& splited.length > 1) {
					Params temp = getParamsByMacroName(splited[0]);
					ArrayList<String> values = new ArrayList<String>();
					for(int j = 1; j < splited.length; j++) {
						values.add(String.valueOf(splited[j]));
					}
					ParamsWithValue param = new ParamsWithValue(temp.params,values,macroNames.get(macroNames.indexOf(splited[i])));
					paramsValue.add(param);
				}
				else if((index = parameters.indexOf(splited[i])) != -1) {
					splited[i] = "#"+String.valueOf(index);
				}
				line += " "+splited[i];
			}
			
			MDT.add(line);
			if(line.contains("MEND")) {
				break;
			}
		}
	}
	
	void printOutput(){
		int i;
		System.out.println("\n**MDT**");
		for(i = 0; i < MDT.size(); i++) {
			System.out.println(MDT.get(i));
		}
		System.out.println();
		System.out.println("\n**MNT**");
		for(i = 0; i < MNT.size(); i++) {
			System.out.println(MNT.get(i).toString());
		}
		System.out.println();
		System.out.println("\n**FORMAL -> POSITIONAL**");
		for(i = 0; i < paramList.size(); i++) {
			System.out.println(paramList.get(i).toString());
		}
		System.out.println();
		System.out.println("\n**POSITIONAL -> ACTUAL**");
		for(i = 0; i < paramsValue.size(); i++) {
			System.out.println(paramsValue.get(i).toString());
		}
//		System.out.println(paramsValue.get(0).toString());
	}
	
	boolean isMacroCall(String macroName){
		return macroNames.contains(macroName);
	}
	
	Params getParamsByMacroName(String macroName) {
		int index;
		if((index = macroNames.indexOf(macroName)) != -1) {
			return paramList.get(index-1);
		}
		return null;
	}
	
	public static void main(String[] args) {
		new Week3();
	}

}


