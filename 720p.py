import bpy

# 720p preset
bpy.context.scene.render.display_mode = 'NONE'
bpy.ops.script.python_file_run(filepath="/usr/share/blender/scripts/presets/render/HDTV_720p.py")
bpy.context.scene.render.antialiasing_samples = '16'
bpy.context.scene.render.image_settings.file_format = 'H264'
bpy.types.ImageFormatSettings.file_format = 'H264'
bpy.ops.script.python_file_run(filepath="/usr/share/blender/scripts/presets/ffmpeg/h264.py")
bpy.context.scene.render.ffmpeg.video_bitrate = 32000
bpy.context.scene.render.ffmpeg.audio_codec = 'MP3'
