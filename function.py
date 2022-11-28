@action(detail=True, methods =['get'], url_path='download', permission_classes=[permissions.AllowAny])
    def download(self, request, pk):
        try:
            document_file=DocumentModel.objects.get(id=pk)
            file_path=document_file.document.path
            print(file_path)
            if os.path.exists(file_path):
                with open(file_path, 'rb') as fh:
                    response=HttpResponse(fh.read(), content_type=mimetypes.guess_type(file_path)[0])
                    response['Content-Disposition'] = "Inline; filename={}".format(os.path.basename(file_path))
                    response['Content-Length'] = os.path.getsize(file_path)
                    return response
            else:        
                return Response({'error' : 'There is no document file of the user'}, status=status.HTTP_403_FORBIDDEN)

        except DocumentModel.DoesNotExist as e:
            return Response({'error': 'Document does not exists for this user'}, status=status.HTTP_404_NOT_FOUND)

    
