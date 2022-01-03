from utilities.db.db_manager import dbManager

class VIDEOS:

    @staticmethod
    def addVideo(videoName, videoURL):
        query_result = dbManager.commit(
            "insert into videos(videoName, videoURL) VALUES ( '%s', '%s')" %
            (videoName, videoURL))
        return query_result

    @staticmethod
    def getAllVideos():
        return dbManager.fetch("select * from videos")


