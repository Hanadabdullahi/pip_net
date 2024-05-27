args = {
    'dataset': 'CUB-200-2011',
    'validation_size': 0.0,
    'net': 'convnext_tiny_26',
    'batch_size': 64,
    'batch_size_pretrain': 128,
    'epochs': 60,
    'optimizer': 'Adam',
    'lr': 0.05,
    'lr_block': 0.0005,
    'lr_net': 0.0005,
    'weight_decay': 0.0,
    'disable_cuda': False,
    'log_dir': './runs/pipnet_cub_cnext26',
    'num_features': 0,
    'image_size': 224,
    'state_dict_dir_net': '',
    'freeze_epochs': 10,
    'dir_for_saving_images': 'Visualization_results',
    'disable_pretrained': False,
    'epochs_pretrain': 10,
    'weighted_loss': False,
    'seed': 1,
    'gpu_ids': '',
    'num_workers': 8,
    'bias': False
}
print(f"Seed value: {args['num_workers']}")