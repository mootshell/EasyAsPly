# Easy As PLY
A simple C++ .ply file parser.

Using it is as easy as pie (Pie not included):

Reading
```c++
// Reader's data and format are deleted when it goes out of scope
EasyAsPLY::PlyReader reader;

reader.Open();
if (reader.Read("YOUR_FILEPATH"))
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
	}
}
reader.Close();
```

Writing
```c++
EasyAsPLY::PlyWriter writer;

EasyAsPLY::PlyFormat* yourFormat;
EasyAsPLY::PlyData* yourData;

writer.Open(yourFormat, yourData);
writer.Write("YOUR_FILEPATH");
writer.Close();
```