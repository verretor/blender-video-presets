import bpy

# 720p preset
bpy.context.scene.render.display_mode = 'NONE'
bpy.context.scene.render.resolution_x = 1280
bpy.context.scene.render.resolution_y = 720
bpy.context.scene.render.resolution_percentage = 100
bpy.context.scene.render.pixel_aspect_x = 1
bpy.context.scene.render.pixel_aspect_y = 1
# Adjust frame rate accordingly
# fps 30 with base 1.001 = 29.97 fps.
bpy.context.scene.render.fps = 30
bpy.context.scene.render.fps_base = 1.000

bpy.context.scene.render.antialiasing_samples = '16'
bpy.context.scene.render.image_settings.file_format = 'H264'
bpy.types.ImageFormatSettings.file_format = 'H264'

is_ntsc = (bpy.context.scene.render.fps != 25)

bpy.context.scene.render.ffmpeg.format = "H264"
bpy.context.scene.render.ffmpeg.codec = "H264"

if is_ntsc:
    bpy.context.scene.render.ffmpeg.gopsize = 18
else:
    bpy.context.scene.render.ffmpeg.gopsize = 15

bpy.context.scene.render.ffmpeg.video_bitrate = 32000
bpy.context.scene.render.ffmpeg.maxrate = 9000
bpy.context.scene.render.ffmpeg.minrate = 0
bpy.context.scene.render.ffmpeg.buffersize = 224 * 8
bpy.context.scene.render.ffmpeg.packetsize = 2048
bpy.context.scene.render.ffmpeg.muxrate = 10080000

bpy.context.scene.render.ffmpeg.audio_codec = 'MP3'
