from llama_cpp import Llama

class QwenModel:
    #def __init__(self, model_path:str = "/home/howard/EdgeEndCol/DeepS$    def __init__(self, model_path: str = "/home/howard/Qwen-7B-Chat.Q4_$        #print(f"CUDA support: {llama_cpp.llama_cuda_supported()}/n")
        self.model = Llama(
            model_path=model_path,
            #n_ctx=2048,
            #n_thread=4,
            n_gpu_layers=12
        )  # 设置>$
        #print(f"GPU加速: {self.model.gpu_supported()}")


    def infer(self, text: str):
        """
        运行推理
        """
        if not text:
            return {"error": "输入文本不能为空"}

        output = self.model(text, max_tokens=200)  # 生成最多 200 个 t$
        return output  # 直接返回推理结果
