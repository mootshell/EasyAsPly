#include <PlyReader.h>
#include <PlyWriter.h>
#include <vector>
#include <iostream>

int main(int argc, char* argv[])
{
	EasyAsPLY::PlyReader reader;
	EasyAsPLY::PlyWriter writer;

	reader.Open();
	if (reader.Read("input"))
	{
		// Get all the vertices
		int vertexIndex = reader.GetFormat()->GetElementIndex("vertex");
		std::vector<EasyAsPLY::PlyElement*>* vertices = reader.GetData()->GetElements(vertexIndex);

		// Get the first vertex
		EasyAsPLY::PlyElement* firstVertex = vertices->at(0);

		// Make sure the x component of the first vertex is a float
		if (reader.GetFormat()->GetElement("vertex")->GetProperty("x")->GetType() == EasyAsPLY::PlyPropertyType::FLOAT)
		{
			// Get the x component of the first vertex
			int xIndex = reader.GetFormat()->GetElement("vertex")->GetPropertyIndex("x");
			float x = firstVertex->GetProperty(xIndex)->GetValue<float>();

			std::cout << x << "\n";
		}
		else
		{
			std::cout << "Not a float\n";
		}
	}
	else
	{
		std::cout << "Parsing failed\n";
		reader.Close();
		return -1;
	}

	writer.Open(reader.GetFormat(), reader.GetData());

	writer.Write("output");
	reader.Close();
	//writer.Close(); TODO
	return 0;
}